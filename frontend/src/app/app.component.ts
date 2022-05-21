import { Component } from '@angular/core';
import { BasketService } from './basket/basket.service';
import { ApiService } from './api.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';
  categoryList: any = [];
  basket: number[] = [0];
  constructor(
    private basketService: BasketService,
    private apiService: ApiService
    )
   {
    this.basketService.basket$.subscribe((data: number[]) => {
      this.basket = data;
    });
    this.getCategoryList({});
   }

  getCategoryList(pars: any) {
      this.apiService.getCategoryList(pars).subscribe((res: any) => {
      this.categoryList = res;
    });

  }

}

