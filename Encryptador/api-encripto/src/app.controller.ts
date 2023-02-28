import { Controller, Get, Put, Delete, Param, Body } from '@nestjs/common';
import { Serialize } from './interceptors/Serialize.interceptor';
import { AppService } from './app.service';
import { ElementDto } from './models/element.dto';

@Controller('encripto')
@Serialize(ElementDto)
export class AppController {

  constructor(private service: AppService){}

  @Get('/healthcheck')
  getHelathCheck(): string {
    return new Date().toDateString();
  }

  @Get('/element/:id')
  getElement(@Param('id') id: string) {
    return this.service.getElement(id);
  }

  @Get('/elements')
  getElements(): string {
    return this.service.getElements();
  }

  @Put('/element')
  putElement(@Body() elementParam: ElementDto) {
    return this.service.createElement(elementParam);
  }

  @Delete('/elemento/:id')
  deleteElement(@Param('id') id: string) {
    return this.service.removeElement(id);
  }


}
