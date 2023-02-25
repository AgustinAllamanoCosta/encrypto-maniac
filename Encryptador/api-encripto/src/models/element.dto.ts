import { IsString } from 'class-validator';

export class ElementDto {

  @IsString()
  name: string;

  @IsString()
  description: string;
  
  @IsString()
  user: string;

  @IsString()
  password: string;
}