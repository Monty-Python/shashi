import { Component, OnInit } from '@angular/core';
import {ServicesService} from '../services/common/services.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  user = {
    username: '',
    password: '',
    email: '',
    reader: '',
    author: '',
    paid: ''
  }

  constructor(
    public commonService: ServicesService,
  ) { }

  ngOnInit() {
  }

  register() {
    // TODO: check if all fields and filled
    // integrate payment gateway
    console.log(this.user);
    this.commonService.post('register/', this.user).subscribe(res => {
      console.log('server response: ', res);
    });
  }

}
