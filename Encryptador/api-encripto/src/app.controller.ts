import { Controller, Get } from '@nestjs/common';

@Controller('encripto')
export class AppController {

  @Get('/healthcheck')
  getHelathCheck(): string {
    return new Date().toDateString();
  }
}
