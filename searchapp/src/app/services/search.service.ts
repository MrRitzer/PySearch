import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, interval, Observable, startWith, Subscription, switchMap } from 'rxjs';
import { Key } from 'src/app/models/key';

const SERVER_URL = 'http://localhost:4000/api/';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  timeInterval: Subscription;


  scored: BehaviorSubject<any> = new BehaviorSubject([]);

  constructor(private http: HttpClient) {
    const observer = {
      next: (response: any) => {
        if (response.data == "Can poll") {
          this.getScored()
        }
      },
      error: (e: string) => {
        console.error('Request failed with error: ' + e);
      }
    }
    this.timeInterval = interval(2500).subscribe(
      tick => {
        this.poll().subscribe(observer)
      }
    );
  }

  newSearch(url: string, keywords: Key[]): void {
    const observer = {
      next: (response: any) => {
        console.log(response.data)
      },
      error: (e: string) => {
        console.error('Request failed with error: ' + e);
      }
    }
    this._newSearch(url,keywords).subscribe(observer)
  }

  private _newSearch(url: string, keywords: Key[]): Observable<string> {
    let apiUrl = SERVER_URL + "startcrawl";
    let body = {
      "url": url,
      "keywords": keywords
    };
    let options = {
      headers: {
        'Content-Type': 'application/json'
      },
      maxRedirects: 20,
    };
    return this.http.post<any>(apiUrl,body,options)
  }

  continueSearch(): void {
    const observer = {
      next: (response: any) => {
        console.log(response.data)
      },
      error: (e: string) => {
        console.error('Request failed with error: ' + e);
      }
    }
    this._continueSearch().subscribe(observer)
  }

  private _continueSearch(): Observable<string> {
    let apiUrl = SERVER_URL + "crawl";
    let options = {
      headers: {
        'Content-Type': 'application/json'
      },
      maxRedirects: 20,
    };
    return this.http.get<any>(apiUrl,options)
  }

  poll(): Observable<any> {
    let apiUrl = SERVER_URL + "poll";
    let options = {
      headers: {
        'Content-Type': 'application/json'
      },
      maxRedirects: 20,
    };
    return this.http.get<any>(apiUrl,options)
  }

  getScored() {
    const observer = {
      next: (response: any) => {
        this.scored.next(response);
      },
      error: (e: string) => {
        console.error('Request failed with error: ' + e);
      }
    }
    this._getScored().subscribe(observer)
  }

  private _getScored(): Observable<string[]> {
    let apiUrl = SERVER_URL + "getformal";
    let options = {
      headers: {
        'Content-Type': 'application/json'
      },
      maxRedirects: 20,
    };
    return this.http.get<any>(apiUrl,options)
  }

  private _test(): Observable<string[]> {
    let apiUrl = SERVER_URL + "test";
    let body = {
      test: 'test'
    }
    let options = {
      headers: {
        'Content-Type': 'application/json'
      },
      maxRedirects: 20,
    };
    return this.http.post<any>(apiUrl,body,options)
  }
}
