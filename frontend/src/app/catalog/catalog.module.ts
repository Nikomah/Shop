import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';
import { SubcategoryComponent } from '../subcategory/subcategory.component';
import { Subcat2Component } from '../subcat2/subcat2.component';
import { Subcat3Component } from '../subcat3/subcat3.component';
import { Subcat4Component } from '../subcat4/subcat4.component';
import { ProductComponent } from '../product/product.component';
import { RouterModule, Routes } from '@angular/router';
import {FlexLayoutModule} from "@angular/flex-layout";
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { ApiService } from '../api.service'

const routes: Routes = [
  {    path: '', component: ListComponent  },
  {    path: 'cat/:catId', component: ListComponent  },
  {    path: 'prod/:prodId', component: ListComponent  },
  {    path: 'subcat2/:sub2Id', component: ListComponent  },
  {    path: 'subcat3/:sub3Id', component: ListComponent  },
  {    path: 'subcat4/:sub4Id', component: ListComponent  }
];


@NgModule({
  declarations: [
    ListComponent,
    SubcategoryComponent,
    ProductComponent,
    Subcat2Component,
    Subcat3Component,
    Subcat4Component,
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
