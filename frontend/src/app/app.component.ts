import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CreditoService } from './services/credito.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  termoBusca: string = '';
  tipoFiltro: 'nfse' | 'credito' = 'nfse';
  resultados: any[] = [];
  erroMensagem: string = '';
  carregando: boolean = false;

  constructor(private creditoService: CreditoService) {}

  realizarConsulta(): void {
    if (!this.termoBusca.trim()) {
      this.erroMensagem = 'Por favor, digite um número para buscar.';
      return;
    }

    this.carregando = true;
    this.erroMensagem = '';
    this.resultados = [];

    if (this.tipoFiltro === 'nfse') {
      this.creditoService.buscarPorNfse(this.termoBusca).subscribe({
        next: (data) => {
          this.resultados = data;
          if (this.resultados.length === 0) {
            this.erroMensagem = 'Nenhum crédito encontrado para esta NFS-e.';
          }
          this.carregando = false;
        },
        error: (err) => {
          this.erroMensagem = 'Erro ao consultar a API do back-end.';
          this.carregando = false;
        }
      });
    } else {
      this.creditoService.buscarPorCredito(this.termoBusca).subscribe({
        next: (data) => {
          this.resultados = [data]; // Envolve em array para a tabela exibir uniformemente
          this.carregando = false;
        },
        error: (err) => {
          if (err.status === 404) {
            this.erroMensagem = 'Crédito não encontrado no sistema.';
          } else {
            this.erroMensagem = 'Erro ao consultar a API do back-end.';
          }
          this.carregando = false;
        }
      });
    }
  }
}
