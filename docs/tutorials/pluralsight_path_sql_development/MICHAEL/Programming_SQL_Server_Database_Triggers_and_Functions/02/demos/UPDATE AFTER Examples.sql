USE [WideWorldImporters]
GO

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

/*
  Add in the Boilerplate code to verify that data
  was actually modified. If not, return and save
  the work of the Trigger.

  With this change, we won't see the message when
  no data is modified.
*/
CREATE OR ALTER TRIGGER [Sales].[TU_Orders_AFTER]ON
	[Sales].[Orders]AFTER UPDATE AS
	BEGIN
		DECLARE @insertedRows INT,
				@deletedRows INT,
				@countString VARCHAR(200);

		SET @insertedRows = (SELECT COUNT(*) FROM INSERTED);
		SET @deletedRows = (SELECT COUNT(*) FROM DELETED);
		SET @countString = 'INSERTED Rows: ' + CAST(@insertedRows AS VARCHAR(10)) + ', DELETED Rows: ' + CAST(@deletedRows AS VARCHAR(10));

		RAISERROR(@countString,1,1);
	END;
GO

/*
 The Trigger will be fired REGARDLESS of actual data manipulation.
 Remember, it is the DML Action being called which causes
 the Trigger to execute
*/
UPDATE Sales.Orders SET Comments='Nothing to see here' WHERE OrderID = 0;
GO

UPDATE Sales.Orders SET Comments='Nothing to see here' WHERE OrderID = 10;
GO


DROP TRIGGER [Sales].[TU_Orders_AFTER];
GO

/******************************************
 *
 * Logging UPDATE of Data From a table
 *
 *****************************************/

/*
  Create a DELETE and UPDATE AFTER Trigger to log
  both DELETE and UPDATE DML actions
*/
CREATE OR ALTER TRIGGER [Sales].[TU_Orders_Logging]ON
	[Sales].[Orders]AFTER UPDATEAS
	BEGIN
		IF (ROWCOUNT_BIG() = 0)
			RETURN;

		SET NOCOUNT ON;

		/*
		  Any UPDATE or DELETE should always have at least one
		  row in the DELETED table if data was modified or deleted.

		  If not, exit out and don't do any more work.
		*/
		IF NOT EXISTS (SELECT 1 FROM DELETED)
			RETURN;

		/*
		  Assume this is an UPDATE to start, having both
		  INSERTED and DELETED data
		*/
		DECLARE @operationType nvarchar(16) = 'UPDATE';

		/*
		  EXCEPT is a great tool for getting only what has been modified. Remember,
		  if a row was "examined" for UPDATE, it will be added to the list of rows
		  that had a DML action applied, regardless of an actual data change. In this
		  way, we only get a list where values in the DELETED virtual table actually
		  differ from the new INSERTED table.

		  This example gets ALL columns, not just the ones that were modified. As an
		  audit log, it will essentially store a copy of what the data was in all columns
		  before being modified.

		  There are many other ways to approach this kind of audit table, so use this
		  as a starting place example.
		*/
		SELECT * INTO #ModifiedData FROM (
				SELECT * FROM DELETED
				EXCEPT
				SELECT * FROM INSERTED
		) ModifiedData;

		/*
		  For each row of the modified data, select a JSON document of the previous data to include
		  in the audit log table.
		*/
		INSERT INTO Application.AuditLog ([ModifiedTime], [ModifiedBy], [Operation], [SchemaName], [TableName], [TableID], [OldValues])
			SELECT GETDATE() , SYSTEM_USER, @operationType, 'Sales','Orders',M1.OrderId, M2.oldValues
				FROM #ModifiedData M1
				CROSS APPLY (
					SELECT oldValues=(select * from #ModifiedData WHERE #ModifiedData.OrderID = M1.OrderID FOR JSON PATH)
				) AS M2
	END;
GO


/*
  UPDATE the Sales.Orders table to see what gets logged.
*/
UPDATE Sales.Orders SET ContactPersonID = 45 where orderId <15;

select * from Application.AuditLog;

/*
  Run the exact same statement. A row will actually be modified in the database,
  but nothing changed about the data.
*/
UPDATE Sales.Orders SET ContactPersonID = 45 where orderId <15;

/*
  Because DELETED and INSERTED data were the same, nothing
  is logged on this action.
*/
select * from Application.AuditLog;

