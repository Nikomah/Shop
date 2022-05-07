import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-subcat4',
  templateUrl: './subcat4.component.html',
  styleUrls: ['./subcat4.component.scss']
})
export class Subcat4Component implements OnInit {
  productList: any = [];
  isProd: boolean = true;
  constructor(
    private apiService: ApiService,
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
    if (res.product.length != 0) {this.productList = res} else {this.isProd = false}

    });
  }
}
