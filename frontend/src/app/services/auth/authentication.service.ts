import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';


export interface UserDetails {
  id: string;
  email: string;
  username: string;
  exp: number;
}



@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(private http: HttpClient, private router: Router) { }

  public token: string;
  public user_key = 'user';







  private saveToken(token: string): void {
    localStorage.setItem(this.user_key, token);
    this.token = token;
  }




  public isLoggedIn(): boolean {
    const user = this.getUserDetails();
    if (user) {
      return user.exp > Date.now() / 1000;
    } else {
      return false;
    }
  }




  public getUserDetails(): UserDetails {
    const token = this.getToken();
    let payload;
    if (token) {
      payload = token.split('.')[1];
      payload = window.atob(payload);
      // console.log(payload);
      return JSON.parse(payload);
    } else {
      return null;
    }
  }

  public getToken(): string {
    if (!this.token) {
      this.token = localStorage.getItem(this.user_key);
    }
    return this.token;
  }



  public logout(): void {
    this.token = '';
    window.localStorage.removeItem(this.user_key);
  }

}
