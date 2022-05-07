import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-subcat3',
  templateUrl: './subcat3.component.html',
  styleUrls: ['./subcat3.component.scss']
})
export class Subcat3Component implements OnInit {
  productList: any = [];
  isProd: boolean = true;
  constructor(
    private apiService: ApiService,
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
    if (res.product.length != 0 || res.subcat4.length != 0) {this.productList = res} else {this.isProd = false}

    });
  }
}

