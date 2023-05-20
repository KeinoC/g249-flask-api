// angular
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, HostBinding, OnInit,  Input, SimpleChange, SimpleChanges   } from '@angular/core';



// services
import { ConfigService } from '@app/core/config/config.service';
import { UtilityService } from '@app/core/utility/utility.service';
import { BaseService } from '@core/base/base.service';


// rxjs
import { Subject } from 'rxjs';
import { takeUntil,tap } from 'rxjs/operators';

// misc

import { ENV } from '@env/environment';
import { WMLOptionItemParams, WmlSampleOptionItemParams } from '@windmillcode/wml-options';



@Component({

  selector: 'option-one',
  templateUrl: './option-one.component.html',
  styleUrls: ['./option-one.component.scss'],
  // changeDetection:ChangeDetectionStrategy.OnPush



})
export class OptionOneComponent  {

  constructor(
    public cdref:ChangeDetectorRef,

    public utilService:UtilityService,
    public configService:ConfigService,
    public baseService:BaseService

  ) { }

  classPrefix = this.utilService.generateClassPrefix('OptionOne')


  @Input('params') params: OptionOneParams = new OptionOneParams()


  @HostBinding('class') myClass: string = this.classPrefix(`View`);
  ngUnsub= new Subject<void>()



  toggleChosen(){
    this.params.wmlOptionItem.click()
  }

  ngOnDestroy(){
    this.ngUnsub.next();
    this.ngUnsub.complete()
  }


}



export class OptionOneParams extends WmlSampleOptionItemParams {
  constructor(params:Partial<OptionOneParams>={}){
    super();
    Object.assign(
      this,
      {
        ...params
      }
    )
  }
}


