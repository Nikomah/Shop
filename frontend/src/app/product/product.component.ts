import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {
  productList: any = [];
  isProd: boolean = true;

  constructor(
    private apiService: ApiService,
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
    if (res.product.length != 0 || res.subcat2.length != 0) {this.productList = res} else {this.isProd = false}

    });
  }



}
