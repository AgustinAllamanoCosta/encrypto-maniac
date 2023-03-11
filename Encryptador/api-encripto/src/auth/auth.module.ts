import { Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UserKey } from './entity/user.keys.entity';

@Module({
  imports: [TypeOrmModule.forFeature([UserKey])],
  providers: [AuthService],
  controllers: [AuthController]
})
export class AuthModule {}
