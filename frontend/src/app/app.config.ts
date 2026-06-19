import { ApplicationConfig, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withFetch } from '@angular/common/http';

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    // Removido o "Experimental" conforme sugerido pelo compilador do Angular
    provideZonelessChangeDetection(), 
    provideRouter(routes),
    provideHttpClient(withFetch())
  ]
};
