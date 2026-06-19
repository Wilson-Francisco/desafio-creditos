import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CreditoService {
  private apiUrl = 'http://localhost:8000/api/creditos';

  constructor(private http: HttpClient) {}

  buscarPorNfse(numeroNfse: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/${numeroNfse}`);
  }

  buscarPorCredito(numeroCredito: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/credito/${numeroCredito}`);
  }
}
