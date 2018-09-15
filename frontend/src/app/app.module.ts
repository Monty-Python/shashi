import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';



// pages
import { HomeComponent } from './home/home.component';


// providers
import { AuthenticationService } from './services/auth/authentication.service';
import { ServicesService } from './services/common/services.service';


const appRoutes: Routes = [
  { path: '', component: HomeComponent },
];



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
  ],
  imports: [
    HttpModule,
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
