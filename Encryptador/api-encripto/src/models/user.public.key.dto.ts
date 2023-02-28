import { IsString } from 'class-validator';

export class UserPublicKeyDto {

  @IsString()
  name: string;

  @IsString()
  key: string;
}