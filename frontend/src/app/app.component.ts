import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend'; name = 'Denis! ';  productList: any = {};
  constructor(private http: HttpClient) { }

  getProductList() {
  this.http.get('http://127.0.0.1:8000/api/v1/product').subscribe( (res: any) => {
    this.productList = res;
      });
  console.log(this.productList);

  }
}
