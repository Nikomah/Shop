import { Component, OnInit } from '@angular/core';

import { ApiService } from './../../api.service';
import { BasketService } from './../basket.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {
  basket: any = [];
  total: any = 0;

  constructor(
    private apiService: ApiService,
    private basketService: BasketService
  ) {
    this.apiService.getBasket(this.basketService.basket).subscribe((data: any) => {
    for (let item of data) {
      item.count = 1;
      this.total += Number(item.price);
      };
    this.basket = data;
    });
   }

  ngOnInit(): void {
  }

  doDelFromBasket(id: any) {
    let index = this.basket.findIndex((item: any) => item.id == id);
    this.total -= this.basket[index].count*this.basket[index].price;
    this.basket.splice(index, 1);
    this.basketService.delFromBasket(id);
  }

  plus(id: number) {
    let index = this.basket.findIndex((item: any) => item.id == id);
    this.basket[index].count += 1;
    this.total += Number(this.basket[index].price);
  }

  minus (id: number) {
    let index = this.basket.findIndex((item: any) => item.id == id);
    if (this.basket[index].count > 1) {
      this.basket[index].count -= 1;
      this.total -= this.basket[index].price;
      };
  }

}
