import {Component, OnInit} from '@angular/core';
import {ProdServiceService} from "../services/prod-service.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.scss']
})
export class ProductItemComponent implements OnInit{
  product: any={};
  categoryName:string=""
  productId:number=0
  constructor(private productService: ProdServiceService, private router:Router,private activatedRoute: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.categoryName=this.activatedRoute.snapshot.params["category"]
    this.productId=this.activatedRoute.snapshot.params["productId"]
    // @ts-ignore
    this.product=this.productService.categories.find(item=>item.name=this.categoryName).products[this.productId]
  }


  like() {
    // @ts-ignore
    this.productService.categories.find(item => item.name === this.categoryName).products[this.productId].likes = this.productService.categories.find(item => item.name === this.categoryName).products[this.productId].likes + 1

  }


}
