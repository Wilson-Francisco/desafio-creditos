import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Garante o suporte ao formulário de busca

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule], // Adicionado aqui
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'desafio-frontend';
}
