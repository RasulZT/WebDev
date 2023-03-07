import {Component, OnDestroy, OnInit} from '@angular/core';
import {AlbumService} from "./services/album.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'Lab6';
  albums: any = []
  album: any
  albumPhotos: any = []

  constructor(private albumService: AlbumService) {
  }

  ngOnInit(): void {
    this.getAlbumById()
    this.getAlbumPhotos()
  }

  getAlbumById() {
    this.albumService.getAlbumById(2).subscribe(result => {
      this.album = result
    }, error => {
      console.log(error)
    })
  }

  ngOnDestroy(): void {
  }

  private getAlbumPhotos() {
    this.albumService.getAlbumPhotos(2).subscribe(result => {
      this.albumPhotos = result
    }, error => {
      console.log(error)
    })
  }

  getAlbums(event: any) {
    this.albums = event
  }
}
