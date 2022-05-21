import { Injectable } from '@angular/core';
import { BehaviorSubject, ReplaySubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BasketService {
  basket: number[] = []
  basket$ = new BehaviorSubject<number[]>([]);

  constructor() { }

  addToBasket(id: number) {
    if ( this.isInBasket(id) ) { this.basket.push(id) };
    this.basket$.next(this.basket);
  }

  isInBasket(value: number) {
    return this.basket.indexOf(value) == -1;
  }

  delFromBasket(id: any) {
    this.basket.pop();
    this.basket$.next(this.basket);
  }

  submitBasket() {

  }
}
