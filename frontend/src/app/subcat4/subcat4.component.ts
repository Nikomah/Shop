import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';
import { BasketService } from './../basket/basket.service';


@Component({
  selector: 'app-subcat4',
  templateUrl: './subcat4.component.html',
  styleUrls: ['./subcat4.component.scss']
})
export class Subcat4Component implements OnInit {
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
      this.getSubcat4({subcat4: params['sub4Id']})
      });
   }

  ngOnInit(): void {
  }

  getSubcat4(pars: any) {
    this.apiService.getSubcat4(pars).subscribe((res: any) => {
    this.productList = res;
    if (res.product.length === 0) {this.isProd = false};

    });
  }
  doAddToBasket(id: number) {
    this.basketService.addToBasket(id);
  }
}
