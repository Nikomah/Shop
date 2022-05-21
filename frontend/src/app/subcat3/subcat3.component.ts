import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';
import { BasketService } from './../basket/basket.service';


@Component({
  selector: 'app-subcat3',
  templateUrl: './subcat3.component.html',
  styleUrls: ['./subcat3.component.scss']
})
export class Subcat3Component implements OnInit {
  productList: any = {
    breadcrumbs: []
  };
  isProd: boolean = true;
  constructor(
    private apiService: ApiService,
    private basketService: BasketService,
    private route: ActivatedRoute
  ) {
      this.route.params.subscribe(params => {
      this.getSubcat3({subcat3: params['sub3Id']})
      });
   }

  ngOnInit(): void {
  }

  getSubcat3(pars: any) {
    this.apiService.getSubcat3(pars).subscribe((res: any) => {
    this.productList = res;
    if (res.product.length === 0 && res.subcat4.length === 0) {this.isProd = false};

    });
  }

    doAddToBasket(id: number) {
    this.basketService.addToBasket(id);
  }

}

