import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getCategoryList() {
    return this.http.get(`${environment.backEndUrl}/api/v1/category/`)
  }
}
