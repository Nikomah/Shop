import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';
import { BasketService } from './../basket/basket.service';


@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {
  productList: any = {
  breadcrumbs: []
  };
  isProd: boolean = true;

  constructor(
    private apiService: ApiService,
    private basketService: BasketService,
    private route: ActivatedRoute,
  ) {
      this.route.params.subscribe(params => {
      this.getProductList({prod: params['prodId']})
      });
     }

  ngOnInit(): void {
  }

  getProductList(pars: any) {
    this.apiService.getProductList(pars).subscribe((res: any) => {
    this.productList = res;
    if (res.product.length === 0 && res.subcat2.length === 0) {this.isProd = false;};
    });
  }

  doAddToBasket(id: number) {
    this.basketService.addToBasket(id);
  }

}
