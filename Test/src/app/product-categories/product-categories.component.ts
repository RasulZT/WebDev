import {Component, OnInit} from '@angular/core';
import {ProdServiceService} from "../services/prod-service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-product-categories',
  templateUrl: './product-categories.component.html',
  styleUrls: ['./product-categories.component.scss']
})
export class ProductCategoriesComponent implements OnInit{
  categories: any = [];
  constructor(private productService: ProdServiceService, private router:Router) {
  }
  // @ts-ignore
  ngOnInit(): void{
    this.categories= this.productService.categories
  }


  goToCategoryProducts(category: any) {
    this.router.navigate(['products/'+category.name])
  }
}
