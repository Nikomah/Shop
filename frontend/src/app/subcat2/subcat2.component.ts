import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-subcat2',
  templateUrl: './subcat2.component.html',
  styleUrls: ['./subcat2.component.scss']
})
export class Subcat2Component implements OnInit {
  productList: any = [];
  isProd: boolean = true;
  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
  ) {
      this.route.params.subscribe(params => {
      this.getSubcat2({subcat2: params['sub2Id']})
      });
   }

  ngOnInit(): void {
  }

  getSubcat2(pars: any) {
    this.apiService.getSubcat2(pars).subscribe((res: any) => {
    if (res.product.length != 0 || res.subcat3.length != 0) {this.productList = res} else {this.isProd = false}

    });
  }


}
