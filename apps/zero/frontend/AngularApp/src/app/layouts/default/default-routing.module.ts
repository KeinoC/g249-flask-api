import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ENV } from '@env/environment';
import { DefaultLayoutComponent } from './default-layout/default-layout.component';


let children = [

]
if(ENV.type === "dev"){

}
const routes: Routes = [

  {
    path:"",
    component:DefaultLayoutComponent,
    children

  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DefaultRoutingModule { }
