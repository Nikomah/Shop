import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';
import { RouterModule, Routes } from '@angular/router';
import {FlexLayoutModule} from "@angular/flex-layout";
import { MatCardModule  } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { ApiService } from './../api.service'

const routes: Routes = [
  {    path: '', component: ListComponent  }
];


@NgModule({
  declarations: [
    ListComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    FlexLayoutModule,
    MatCardModule,
    MatButtonModule,
  ],
  providers: [
    ApiService
  ]
})
export class CatalogModule { }
