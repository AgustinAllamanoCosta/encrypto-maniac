import { Test, TestingModule } from '@nestjs/testing';
import { Repository } from 'typeorm';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';
import { UserKey } from './entity/user.keys.entity';

describe.skip('AuthController', () => {
  let controller: AuthController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [AuthController],
      providers: [AuthService,
        {
          provide: Repository<UserKey>,
          useValue: {
            create: jest.fn(),
            save: jest.fn(),
          }
        }
      ]
    }).compile();

    controller = module.get<AuthController>(AuthController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
