import { Component, OnInit } from '@angular/core';
import { ApiService } from './../../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
// export class ListComponent implements OnInit {
//     categoryList: any = {results: []};
//     constructor(
//     private apiService: ApiService,
//     private route: ActivatedRoute
//     ) {
//     this.route.params.subscribe(params => {
//         if(params.hasOwnProperty('catId')) {
//           this.getCategoryList({cat: params['catId']});
//         } else {
//             this.getCategoryList({});
//         }
//       } )
//
//      }
//
//   ngOnInit(): void {
//   }
//
//   getCategoryList(pars: any) {
//    this.apiService.getCategoryList(pars).subscribe((res: any) => {
//     this.categoryList = res;
//     });
//   }
// }


export class ListComponent implements OnInit {
    categoryList: any = {results: []};
    list: string = 'category'
    constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
    )
    { this.route.params.subscribe(params => {
        if(params.hasOwnProperty('catId')) { this.list = 'subcategory'}
        else if(params.hasOwnProperty('prodId')) { this.list = 'product'}
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
