import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../../../environments/environment';
import { ApiService } from './../../api.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {
  categoryList: any = {results: []};
  constructor(private http: HttpClient, private apiService: ApiService) { this.getCategoryList(); }

  ngOnInit(): void {
  }

  getCategoryList() {
   this.apiService.getCategoryList().subscribe((res: any) => {
    this.categoryList = res;
    });
  }
}
