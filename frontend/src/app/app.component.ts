import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../environments/environment';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';
  categoryList: any = {results: []};
  constructor(private http: HttpClient,
                                       )
               {this.getCategoryList();}

  getCategoryList() {
  this.http.get(`${environment.backEndUrl}/api/v1/category/`).subscribe( (res: any) => {
    this.categoryList = res;
    });


//   getCategoryList() {
//   this.http.get(`${environment.backEndUrl}/api/v1/category/`).subscribe( (res: any) => {
//     this.categoryList = res;
//     });
//   console.log(this.categoryList.results);
  }
}

