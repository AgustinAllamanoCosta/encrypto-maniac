import { IsString } from 'class-validator';

export class UserChallengeDto {

  @IsString()
  name: string;

  @IsString()
  token: string;
}