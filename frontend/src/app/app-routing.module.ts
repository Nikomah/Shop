import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'catalog',
    pathMatch: 'full'
  },
  {
    path: 'profile',
    loadChildren: () => import('./profile/profile.module').then(mod => mod.ProfileModule),
  },
  {
    path: 'catalog',
    loadChildren: () => import('./catalog/catalog.module').then(mod => mod.CatalogModule),
  },
  {
    path: 'basket',
    loadChildren: () => import('./basket/basket.module').then(mod => mod.BasketModule),
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    initialNavigation: 'enabledBlocking'
}),
    HttpClientModule],
  exports: [RouterModule]
})
export class AppRoutingModule { }
