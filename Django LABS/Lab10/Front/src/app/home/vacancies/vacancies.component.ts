import {Component, OnInit} from '@angular/core';
import {Vacancy} from "../../core/models/Vacancy";
import {VacancyService} from "../../services/vacancy.service";

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.scss']
})
export class VacanciesComponent implements OnInit {
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }


}
