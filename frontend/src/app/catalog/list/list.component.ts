import { Component, OnInit } from '@angular/core';
import { ApiService } from './../../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})

export class ListComponent implements OnInit {
    categoryList: any = [];
    list = 'category';
    constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
    )
    { this.route.params.subscribe(params => {
        if(params.hasOwnProperty('catId')) { this.list = 'subcategory'}
        else if(params.hasOwnProperty('prodId')) { this.list = 'product'}
        else if(params.hasOwnProperty('sub2Id')) { this.list = 'subcat2'}
        else if(params.hasOwnProperty('sub3Id')) { this.list = 'subcat3'}
        else if(params.hasOwnProperty('sub4Id')) { this.list = 'subcat4'}
        });

      this.getCategoryList({}); }

  ngOnInit(): void {
  }

  getCategoryList(pars: any) {
   this.apiService.getCategoryList(pars).subscribe((res: any) => {
    this.categoryList = res;
    });
  }
}
