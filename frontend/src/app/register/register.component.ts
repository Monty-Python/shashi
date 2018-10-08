import { Component, OnInit } from '@angular/core';
import {ServicesService} from '../services/common/services.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  user = {
    user: {username: 'test1', email: 'tst@email.com', password: '123'},
    is_reader: false,
    is_author: false,
    is_paid: false
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
