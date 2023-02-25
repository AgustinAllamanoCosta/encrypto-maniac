import { Injectable } from '@nestjs/common';
import { ElementDto } from './models/element.dto';

@Injectable()
export class AppService {
  getElement(id: string) {
    throw new Error('Method not implemented.');
  }
  getElements(): string {
    throw new Error('Method not implemented.');
  }
  createElement(elementoParam: ElementDto) {
    throw new Error('Method not implemented.');
  }
  removeElement(id: string) {
    throw new Error('Method not implemented.');
  }

}
