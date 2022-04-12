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
  name = 'Denis! ';
  productList: any = {results: []};
  constructor(private http: HttpClient,
                                       )
               {this.getProductList(); }

  getProductList() {
  this.http.get(`${environment.backEndUrl}/api/v1/product/`).subscribe( (res: any) => {
    this.productList = res;

    });
//   console.log(this.productList.results);
  }
}

