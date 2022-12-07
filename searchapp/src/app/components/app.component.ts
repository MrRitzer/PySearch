import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { Validators } from '@angular/forms';
import { interval, startWith, Subscription, switchMap } from 'rxjs';
import { Key } from 'src/app/models/key';
import { SearchService } from 'src/app/services/search.service';

import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, AfterViewInit {
  @ViewChild('paginator') paginator!: MatPaginator;
  
  timeInterval: Subscription = new Subscription();
  title = 'searchapp';
  keywords: string;
  url: string;
  columns: string[] = ['title']

  dataSource: MatTableDataSource<any> = new MatTableDataSource<any>();

  constructor(private searchService: SearchService) {
    let observer = {
      next: (data: any) => {
        console.log(data)
        this.dataSource.data = data;
        this.dataSource.paginator = this.paginator;
      }
    }
    this.searchService.scored.subscribe(observer)
    // this.url = "http://www.rottentomatoes.com";
    // this.keywords = "black panther";
    this.url = "";
    this.keywords = "";
  }

  ngOnInit() { }

  ngAfterViewInit() {  }

  canSearch(): boolean {
    if (this.url == '' || this.keywords == '')
      return true
    return false
  }

  isValid(): boolean {
    try {
      new RegExp('(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})[/\\w .-]*/?',this.url);
      return true;
    } catch {
      return false;
    }
  }

  search() {
    let newSearch: Key[] = [];
    let str = this.keywords.split(" ");
    str.forEach(element => {
      newSearch.push({key: element})
    });
    this.searchService.newSearch(this.url,newSearch)
  }

  continueSearch() {
    this.searchService.continueSearch()
  }

  canContinue() {
    return !(this.dataSource.data.length > 0)
  }

  next() {
    // this.searchService.continueSearch()
  }
}
