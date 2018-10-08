import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';



// pages
import { HomeComponent } from './home/home.component';


// providers
import { AuthenticationService } from './services/auth/authentication.service';
import { ServicesService } from './services/common/services.service';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ProfileComponent } from './profile/profile.component';


const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'profile', component: ProfileComponent },
];



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    ProfileComponent,
  ],
  imports: [
    HttpModule,
    FormsModule,
    HttpClientModule,
    BrowserModule,
    RouterModule.forRoot(appRoutes),
  ],
  providers: [
    AuthenticationService,
    ServicesService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
