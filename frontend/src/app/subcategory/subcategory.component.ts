import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-subcategory',
  templateUrl: './subcategory.component.html',
  styleUrls: ['./subcategory.component.scss']
})
export class SubcategoryComponent implements OnInit {
  subcategoryList: any = {results: []};
  categoryList: any = {results: []}


  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute

  ) {
       this.route.params.subscribe(params => {

          this.getCategoryList({cat: params['catId']});

      } );
      this.getCategoryList({});
   }

  ngOnInit(): void {
  }

    getCategoryList(pars: any) {
   this.apiService.getCategoryList(pars).subscribe((res: any) => { if(pars.cat) {
    this.subcategoryList = res} else {this.categoryList = res}
    });
  }



}
