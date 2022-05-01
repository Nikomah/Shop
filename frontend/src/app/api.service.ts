import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getCategoryList(pars: any) {
    if(pars.hasOwnProperty('cat')) {
      return this.http.get(`${environment.backEndUrl}/api/v1/category/${pars['cat']}/`)
      } else {
            return this.http.get(`${environment.backEndUrl}/api/v1/category/`);
            }
  }

  getProductList(pars: any) {
    return this.http.get(`${environment.backEndUrl}/api/v1/subcategory/${pars['prod']}/`)
    }
}
