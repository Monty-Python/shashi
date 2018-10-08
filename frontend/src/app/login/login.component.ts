import { Component, OnInit } from '@angular/core';
import { ServicesService } from '../services/common/services.service';
import { AuthenticationService } from '../services/auth/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user = {
    username: 'test1', 
    password: '123'
  }

  constructor(
    public commonService: ServicesService,
    public authService: AuthenticationService,
  ) { }

  ngOnInit() {
  }



  login() {
    this.commonService.post('get-auth-jwt/', this.user).subscribe(res => {
      if (res.token) {
        this.authService.saveToken(res.token);
      } else {
        console.log(res);
      }
    });
  }

}
