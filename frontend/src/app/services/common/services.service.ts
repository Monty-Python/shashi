import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../auth/authentication.service';
import { catchError, map } from 'rxjs/operators';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';




@Injectable({
  providedIn: 'root'
})
export class ServicesService {

  constructor(private http: HttpClient, private router: Router, private auth: AuthenticationService) { }


  public handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error.message);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong,
      console.error(
        `Backend returned code ${error.status}, ` +
        `body was: ${error.error}`);
    }
    return ('');
  }


  server = 'http://localhost:8000/'
  header = { headers: { Authorization: `Bearer ${this.auth.getToken()}` } };

  public get(url: any) {
    // console.log("common get: ", url);
    return this.http.get(this.server + url, this.header).pipe(
      map((data) => {
        return data;
      }),
      catchError(this.handleError));
  }


  public put(url, arg: any) {
    return this.http.put(this.server + url, arg, this.header).pipe(
      map((data) => {
        return data;
      }),
      catchError(this.handleError));
  }


  public post(url, arg: any) {
    console.log(this.header);
    return this.http.post(this.server + url, arg, this.header).pipe(
      map((data) => {
        return data;
      }),
      catchError(this.handleError));
  }



  public delete(url: any) {
    return this.http.delete(this.server + url, this.header).pipe(
      map((data) => {
        return data;
      }),
      catchError(this.handleError));
  }

}
