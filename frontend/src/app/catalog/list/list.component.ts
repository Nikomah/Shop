import { Component, OnInit } from '@angular/core';
import { ApiService } from './../../api.service';

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
//           console.log(`category ${params['catId']}`);
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
    constructor(
    private apiService: ApiService
    )
    { this.getCategoryList({}) }

  ngOnInit(): void {
  }

  getCategoryList(pars: any) {
   this.apiService.getCategoryList(pars).subscribe((res: any) => {
    this.categoryList = res;
    });
  }
}
