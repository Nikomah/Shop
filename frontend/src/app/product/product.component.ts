import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {
  productList: any = {results: []};

  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
  ) {
      this.route.params.subscribe(params => {
      this.getProductList({prod: params['prodId']})
      });
     }

  ngOnInit(): void {
  }

  getProductList(pars: any) {
    this.apiService.getProductList(pars).subscribe((res: any) => {
      this.productList = res
    });
  }



}
