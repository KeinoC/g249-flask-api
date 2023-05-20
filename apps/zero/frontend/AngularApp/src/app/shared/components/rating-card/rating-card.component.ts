// angular
import { ChangeDetectionStrategy, ChangeDetectorRef, Component, HostBinding, OnInit,  Input   } from '@angular/core';



// services
import { ConfigService } from '@app/core/config/config.service';
import { UtilityService } from '@app/core/utility/utility.service';
import { BaseService } from '@core/base/base.service';


// rxjs
import { Subject } from 'rxjs';
import { takeUntil,tap } from 'rxjs/operators';

// misc

import { ENV } from '@env/environment';
import { WMLImage, WMLUIProperty } from '@windmillcode/wml-components-base';



@Component({

  selector: 'rating-card',
  templateUrl: './rating-card.component.html',
  styleUrls: ['./rating-card.component.scss'],
  changeDetection:ChangeDetectionStrategy.OnPush



})
export class RatingCardComponent  {

  constructor(
    public cdref:ChangeDetectorRef,

    public utilService:UtilityService,
    public configService:ConfigService,
    public baseService:BaseService

  ) { }

  classPrefix = this.utilService.generateClassPrefix('RatingCard')


  @Input('params') params: RatingCardParams = new RatingCardParams()


  @HostBinding('class') myClass: string = this.classPrefix(`View`);
  ngUnsub= new Subject<void>()

  ngOnInit(): void {
  }

  ngOnDestroy(){
    this.ngUnsub.next();
    this.ngUnsub.complete()
  }

}



export class RatingCardParams {
  constructor(params:Partial<RatingCardParams>={}){
    Object.assign(
      this,
      {
        ...params
      }
    )
  }
  title:WMLUIProperty;
  subTitle:WMLUIProperty
  desc:WMLUIProperty
  avatar:WMLImage
  rating:number;
}


