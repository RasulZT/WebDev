import {Component, OnInit} from '@angular/core';
import {ProdServiceService} from "../services/prod-service.service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent implements OnInit {
  products: any = []
  category: string = ""

  constructor(private productService: ProdServiceService, private router:Router,private activatedRoute: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.category=this.activatedRoute.snapshot.params["category"]
    // console.log(this.activatedRoute)
    // @ts-ignore
    this.products=this.productService.categories.find(item=>item.name===this.category).products
  }

  goToPage(i:number) {
    this.router.navigate([`products/${this.category}/${i}`])
  }

  removeItem(i: number) {
    this.products=this.products.filter((item: any)=>{
      return item!== this.products[i]
    })
    // @ts-ignore
    this.productService.categories.find(item=>item.name===this.category).products = this.products
  }
}
