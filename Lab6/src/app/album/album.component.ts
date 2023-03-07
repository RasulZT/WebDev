import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {AlbumService} from '../services/album.service';

@Component({
  selector: 'app-album',
  templateUrl: './album.component.html',
  styleUrls: ['./album.component.scss']
})
export class AlbumComponent implements OnInit {
  @Input() albumPhotosChild: any[] = [];
  @Output() outputAlbom = new EventEmitter();

  constructor(private albumService: AlbumService) {
  }

  ngOnInit(): void {
    this.getAlbums()
  }

  getAlbums() {
    this.albumService.getAlbums().subscribe(result => {
      this.outputAlbom.emit(result);
    }, error => {
      console.log(error)
    })
  }
}
